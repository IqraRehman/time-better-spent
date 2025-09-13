import { type House, type InsertHouse } from "@shared/schema";

export interface IStorage {
  createHouseCalculation(house: InsertHouse): Promise<House>;
  getHouseCalculation(id: number): Promise<House | undefined>;
}

export class MemStorage implements IStorage {
  private houses: Map<number, House>;
  private currentId: number;

  constructor() {
    this.houses = new Map();
    this.currentId = 1;
  }

  async createHouseCalculation(insertHouse: InsertHouse): Promise<House> {
    const id = this.currentId++;
    const house: House = { ...insertHouse, id };
    this.houses.set(id, house);
    return house;
  }

  async getHouseCalculation(id: number): Promise<House | undefined> {
    return this.houses.get(id);
  }
}

export const storage = new MemStorage();
